
  const planSelect = document.getElementById('plan');
  const customizationInput = document.getElementById('customizationInput');
  const preferredDateInput = document.getElementById('preferredDate');

  planSelect.addEventListener('change', () => {
    const selectedPlan = planSelect.value;
    if (selectedPlan === 'starter') {
      customizationInput.classList.add('hidden');
    } else {
      customizationInput.classList.remove('hidden');
    }
  });

  // Set min attribute for preferredDateInput to today's date
  const today = new Date().toISOString().split('T')[0]; // Get today's date in "YYYY-MM-DD" format
  preferredDateInput.setAttribute('min', today);

  document.addEventListener("DOMContentLoaded", function() {
    // Get all elements with class "scrollToFormButton"
    const scrollToFormButtons = document.querySelectorAll(".scrollToFormButton");

    // Get the form element
    const form = document.getElementById("myForm");

    // Add click event listener to each button
    scrollToFormButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            // Scroll to the form using smooth behavior
            form.scrollIntoView({ behavior: 'smooth' });
        });
    });
});


