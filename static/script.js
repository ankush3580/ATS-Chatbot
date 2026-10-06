let TECHNICAL_SKILLS = [];


async function loadSkills() {

    const response = await fetch(
        "/static/skills.json"
    );

    if (!response.ok) {
        throw new Error(
            "Could not load skills.json"
        );
    }

    TECHNICAL_SKILLS = await response.json();
}
const STOP_WORDS = new Set([
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "has",
    "have",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "that",
    "the",
    "their",
    "this",
    "to",
    "was",
    "were",
    "will",
    "with",
    "we",
    "you",
    "your",
    "our",
    "they",
    "them",
    "these",
    "those",
    "which",
    "who",
    "what",
    "when",
    "where",
    "how",
    "can",
    "could",
    "should",
    "would",
    "into",
    "about",
    "than",
    "then",
    "also"
]);

/*
 * ---------------------------------------------------------
 * TEXT PARSING AND STRING MANIPULATION
 * ---------------------------------------------------------
 */

function cleanText(text) {

    text = text.toLowerCase();

    // Normalize common separators
    text = text.replace(/[/|,;:()[\]{}]/g, " ");

    // Preserve technical characters such as +, # and .
    text = text.replace(/[^a-z0-9+#.\s]/g, " ");

    // Remove repeated whitespace
    text = text.replace(/\s+/g, " ");

    return text.trim();
}


function tokenize(text) {

    const cleanedText = cleanText(text);

    if (!cleanedText) {
        return [];
    }

    const words = cleanedText.split(" ");

    return words.filter(
        word => word.length > 1 && !STOP_WORDS.has(word)
    );
}


/*
 * ---------------------------------------------------------
 * PATTERN MATCHING / SKILL EXTRACTION
 * ---------------------------------------------------------
 */

function skillFound(skill, text) {

    const escapedSkill = skill.replace(
        /[.*+?^${}()|[\]\\]/g,
        "\\$&"
    );

    const pattern =
        new RegExp(
            "(?<![a-z0-9+#])" +
            escapedSkill +
            "(?![a-z0-9+#])",
            "i"
        );

    return pattern.test(text);
}


function extractSkills(text) {

    const foundSkills = [];

    for (const skill of TECHNICAL_SKILLS) {

        if (skillFound(skill, text)) {
            foundSkills.push(skill);
        }
    }

    return foundSkills.sort();
}


/*
 * ---------------------------------------------------------
 * TF-IDF
 * ---------------------------------------------------------
 */

function calculateTermFrequency(tokens) {

    const frequency = {};

    for (const token of tokens) {

        frequency[token] =
            (frequency[token] || 0) + 1;
    }

    const totalWords = tokens.length;

    if (totalWords === 0) {
        return {};
    }

    const tf = {};

    for (const word in frequency) {

        tf[word] =
            frequency[word] / totalWords;
    }

    return tf;
}


function calculateIDF(documents) {

    const documentFrequency = {};
    const totalDocuments = documents.length;

    for (const document of documents) {

        const uniqueWords = new Set(document);

        for (const word of uniqueWords) {

            documentFrequency[word] =
                (documentFrequency[word] || 0) + 1;
        }
    }

    const idf = {};

    for (const word in documentFrequency) {

        idf[word] =
            Math.log(
                (totalDocuments + 1) /
                (documentFrequency[word] + 1)
            ) + 1;
    }

    return idf;
}


function createTfidfVector(tokens, idf, vocabulary) {

    const tf = calculateTermFrequency(tokens);

    const vector = [];

    for (const word of vocabulary) {

        const termFrequency = tf[word] || 0;
        const inverseDocumentFrequency = idf[word] || 0;

        vector.push(
            termFrequency * inverseDocumentFrequency
        );
    }

    return vector;
}


/*
 * ---------------------------------------------------------
 * COSINE SIMILARITY
 * ---------------------------------------------------------
 */

function cosineSimilarity(vectorA, vectorB) {

    let dotProduct = 0;
    let magnitudeA = 0;
    let magnitudeB = 0;

    for (let i = 0; i < vectorA.length; i++) {

        dotProduct += vectorA[i] * vectorB[i];

        magnitudeA += vectorA[i] * vectorA[i];

        magnitudeB += vectorB[i] * vectorB[i];
    }

    magnitudeA = Math.sqrt(magnitudeA);
    magnitudeB = Math.sqrt(magnitudeB);

    if (magnitudeA === 0 || magnitudeB === 0) {
        return 0;
    }

    return dotProduct / (magnitudeA * magnitudeB);
}


function calculateSimilarity(resumeText, jdText) {

    const resumeTokens = tokenize(resumeText);
    const jdTokens = tokenize(jdText);

    const documents = [
        resumeTokens,
        jdTokens
    ];

    const idf = calculateIDF(documents);

    const vocabularySet = new Set([
        ...resumeTokens,
        ...jdTokens
    ]);

    const vocabulary = Array.from(vocabularySet);

    const resumeVector =
        createTfidfVector(
            resumeTokens,
            idf,
            vocabulary
        );

    const jdVector =
        createTfidfVector(
            jdTokens,
            idf,
            vocabulary
        );

    return cosineSimilarity(
        resumeVector,
        jdVector
    );
}


/*
 * ---------------------------------------------------------
 * ATS SCORE
 * ---------------------------------------------------------
 */

function calculateATSScore(
    similarityScore,
    matchingSkills,
    jdSkills
) {

    let skillScore = 0;

    if (jdSkills.length > 0) {

        skillScore =
            matchingSkills.length /
            jdSkills.length;
    }

    /*
     * 60% skill matching
     * 40% textual similarity
     */

    const atsScore =
        (
            skillScore * 0.60 +
            similarityScore * 0.40
        ) * 100;

    return Number(atsScore.toFixed(2));
}


/*
 * ---------------------------------------------------------
 * SUGGESTION ENGINE
 * ---------------------------------------------------------
 */

function generateSuggestions(
    missingSkills,
    similarityScore,
    atsScore
) {

    const suggestions = [];

    if (missingSkills.length > 0) {

        suggestions.push(
            "Consider adding relevant experience or projects involving: " +
            missingSkills.join(", ") +
            ", if you genuinely have those skills."
        );
    }

    if (similarityScore < 0.40) {

        suggestions.push(
            "The resume has relatively low textual similarity " +
            "with the job description. Consider tailoring your " +
            "project and experience descriptions to the role."
        );

    } else if (similarityScore < 0.70) {

        suggestions.push(
            "The resume has moderate similarity with the job " +
            "description. Consider using more relevant terminology " +
            "from the job description where accurate."
        );

    } else {

        suggestions.push(
            "The resume has strong textual similarity with the " +
            "job description."
        );
    }


    if (atsScore < 50) {

        suggestions.push(
            "Consider improving alignment between the resume " +
            "and the job requirements."
        );

    } else if (atsScore < 70) {

        suggestions.push(
            "The resume has moderate alignment with the job " +
            "requirements. Addressing missing skills may improve the score."
        );

    } else {

        suggestions.push(
            "The resume shows strong alignment with the analyzed " +
            "job description."
        );
    }

    return suggestions;
}


/*
 * ---------------------------------------------------------
 * COMPLETE ATS ANALYSIS
 * ---------------------------------------------------------
 */

function analyzeResume(resumeText, jdText) {

    const cleanedResume = cleanText(resumeText);
    const cleanedJD = cleanText(jdText);

    const resumeSkills =
        extractSkills(cleanedResume);

    const jdSkills =
        extractSkills(cleanedJD);

    const matchingSkills =
        resumeSkills.filter(
            skill => jdSkills.includes(skill)
        );

    const missingSkills =
        jdSkills.filter(
            skill => !resumeSkills.includes(skill)
        );

    const similarity =
        calculateSimilarity(
            cleanedResume,
            cleanedJD
        );

    const atsScore =
        calculateATSScore(
            similarity,
            matchingSkills,
            jdSkills
        );

    const suggestions =
        generateSuggestions(
            missingSkills,
            similarity,
            atsScore
        );

    return {

        atsScore: atsScore,

        similarity:
            Number((similarity * 100).toFixed(2)),

        resumeSkills: resumeSkills,

        jdSkills: jdSkills,

        matchingSkills: matchingSkills,

        missingSkills: missingSkills,

        suggestions: suggestions
    };
}