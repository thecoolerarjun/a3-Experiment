function startButtonFunc() {
    var sampleButton = document.getElementById("sampleButton");
    if (sampleButton.style.visibility == "hidden") {
        sampleButton.style.visibility = "visible";
    } else {
        sampleButton.style.visibility = "hidden";
    }
}