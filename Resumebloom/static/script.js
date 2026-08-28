async function analyzeResume() {

    const resume = document.getElementById("resume").value.trim();
    const jobDescription =
        document.getElementById("jobDescription").value.trim();

    const button = document.getElementById("analyzeBtn");
    const error = document.getElementById("error");

    error.textContent = "";

    if (!resume || !jobDescription) {
        error.textContent =
            "🌷 Please add both your resume and the target job description.";
        return;
    }

    button.disabled = true;
    button.innerHTML = "Blooming your resume... 🌱";

    try {

        const response = await fetch("/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                resume: resume,
                job_description: jobDescription
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Something went wrong.");
        }

        displayResults(data);

    } catch (err) {

        error.textContent = "🌧️ " + err.message;

    } finally {

        button.disabled = false;
        button.innerHTML = "Bloom my resume 🌷";
    }
}


function displayResults(data) {

    document.getElementById("results").classList.remove("hidden");

    document.getElementById("score").textContent =
        data.score + "/100";

    document.getElementById("summary").textContent =
        data.summary;


    // Strengths

    const strengths = document.getElementById("strengths");

    strengths.innerHTML = "";

    data.strengths.forEach(item => {

        const li = document.createElement("li");

        li.textContent = item;

        strengths.appendChild(li);
    });


    // Keywords

    const keywords = document.getElementById("keywords");

    keywords.innerHTML = "";

    data.missing_keywords.forEach(keyword => {

        const tag = document.createElement("span");

        tag.className = "tag";

        tag.textContent = keyword;

        keywords.appendChild(tag);
    });


    // Improvements

    const improvements =
        document.getElementById("improvements");

    improvements.innerHTML = "";

    data.improvements.forEach(item => {

        const div = document.createElement("div");

        div.className = "improvement";

        div.innerHTML = `
            <strong>${escapeHtml(item.problem)}</strong>
            <span>${escapeHtml(item.suggestion)}</span>
        `;

        improvements.appendChild(div);
    });


    // Rewritten bullets

    const rewrites =
        document.getElementById("rewrites");

    rewrites.innerHTML = "";

    data.rewritten_bullets.forEach(item => {

        const div = document.createElement("div");

        div.className = "rewrite";

        div.innerHTML = `
            <div class="original">
                Before: ${escapeHtml(item.original)}
            </div>

            <div class="improved">
                After: ${escapeHtml(item.improved)}
            </div>
        `;

        rewrites.appendChild(div);
    });


    // Interview questions

    const questions =
        document.getElementById("questions");

    questions.innerHTML = "";

    data.interview_questions.forEach(question => {

        const li = document.createElement("li");

        li.textContent = question;

        questions.appendChild(li);
    });


    document.getElementById("results")
        .scrollIntoView({
            behavior: "smooth"
        });
}


function escapeHtml(text) {

    const div = document.createElement("div");

    div.textContent = text;

    return div.innerHTML;
}