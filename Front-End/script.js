async function searchJobs() {
    const url = document.getElementById("url").value;
    const keyword = document.getElementById("keyword").value;
    const page = document.getElementById("page").value;

    if (!url || !keyword || !page) {
        alert("Please fill all fields!");
        return;
    }

    const res = await fetch(
        `http://127.0.0.1:8000/jobs?url=${encodeURIComponent(url)}&keyword=${encodeURIComponent(keyword)}&page=${page}`
    );
    const data = await res.json();

    let html = '';
    if (data.total_results === 0) {
        html = "<p>No jobs found.</p>";
    } else {
        data.results.forEach(job => {
            html += `
                <div class="job-card">
                    <div class="job-title">${job.job_title}</div>
                    <div class="job-company">${job.company}</div>
                    <div class="job-location">${job.location}</div>
                </div>
            `;
        });
    }

    document.getElementById("results").innerHTML = html;
}