const birthdayInput = document.getElementById('dob-input');
const ageInput = document.getElementById('age-text');

birthdayInput.addEventListener("change", () => {
    const birthday = new Date(birthdayInput.value)
    const today = new Date();

    if(birthday > today) {
        window.alert('Invalid Date of Birth');
        birthdayInput.value = '';
    }

    const age = today.getFullYear() - birthday.getFullYear();

    if(age < 18) {
        window.alert("We can't hire underage employees");
        birthdayInput.value = '';
    }
    else {
        ageInput.value = age;
    }
});

const cancelBtn = document.getElementsByClassName('cancel-btn')[0];

cancelBtn.addEventListener("click", () => {
    window.location = "employee_list";
})