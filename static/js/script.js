copyPhoneNumber = () => {
  //get the text to copy
  var textToCopy = document.querySelector("#phoneNumberResult");
  //focus on the text box and select the text
  textToCopy.focus();
  textToCopy.select();
  //copy to clipboard
  document.execCommand("copy");
  //get the copied success notification and make it visible
  let numberCopyNotification = document.querySelector(
    ".phoneNumberCopyNotification"
  );
  numberCopyNotification.classList.remove("hidden");
};

copyEmailAdress = () => {
  //get the text to copy
  var textToCopy = document.querySelector("#emailResult");
  //focus on the text box and select the text
  textToCopy.focus();
  textToCopy.select();
  //copy to clipboard
  document.execCommand("copy");
  //get the copied success notification and make it visible
  let emailCopyNotification = document.querySelector(".emailCopyNotification");
  emailCopyNotification.classList.remove("hidden");
};

let phoneNumberCopyBtn = document.querySelector(".copyPhoneNumberBtn");
phoneNumberCopyBtn.addEventListener("click", copyPhoneNumber);

let emailAdressCopyBtn = document.querySelector(".copyEmailBtn");
emailAdressCopyBtn.addEventListener("click", copyEmailAdress);
