// Mark task as completed when clicking checkbox
document.addEventListener("DOMContentLoaded", function() {
    const checkboxes = document.querySelectorAll(".checkbox");
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener("change", function() {
            const index = this.getAttribute("data-index");
            window.location.href = `/check/${index}`;
        });
    });
});
