document.addEventListener("DOMContentLoaded", () => {

    // ===========================
    // Upload Success Animation
    // ===========================

    const resumeInput = document.getElementById("resume");

    const uploadIcon = document.getElementById("uploadIcon");

    const uploadTitle = document.getElementById("uploadTitle");

    const uploadText = document.getElementById("uploadText");

    const fileName = document.getElementById("fileName");

    const uploadBox = document.querySelector(".upload-box");

    if(resumeInput){

        resumeInput.addEventListener("change", function(){

            if(this.files.length > 0){

                uploadIcon.innerHTML = "✅";

                uploadTitle.innerHTML = "Resume Uploaded";

                uploadText.innerHTML = "Ready for AI Analysis";

                fileName.innerHTML = this.files[0].name;

                uploadBox.style.border = "2px solid #22c55e";

                uploadBox.style.boxShadow = "0 0 30px rgba(34,197,94,.35)";

                uploadBox.style.transform = "scale(1.02)";

            }

        });

    }

    // ===========================
    // AI Loading Screen
    // ===========================

    const form = document.querySelector("form");

    if(form){

        form.addEventListener("submit", function(e){

            e.preventDefault();

            const loader = document.getElementById("loader");

            loader.style.display = "flex";

            const steps = [

                "📄 Extracting Resume...",

                "🧠 Performing Semantic Analysis...",

                "🎯 Matching Resume Skills...",

                "📊 Calculating ATS Score...",

                "💡 Generating AI Recommendations...",

                "📑 Preparing Professional Report...",

                "✅ Analysis Complete..."

            ];

            let index = 0;

            const text = document.getElementById("loadingText");

            text.innerHTML = steps[0];

            const timer = setInterval(()=>{

                index++;

                if(index < steps.length){

                    text.innerHTML = steps[index];

                }else{

                    clearInterval(timer);

                    setTimeout(()=>{

                        form.submit();

                    },700);

                }

            },650);

        });

    }

});