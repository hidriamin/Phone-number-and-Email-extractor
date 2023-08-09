copyPhoneNumber = () => {
  //get the text to copy
  var textToCopy = document.querySelector("#phoneNumberResult");
  //focus on the text box and select the text
  textToCopy.focus();
  textToCopy.select();
  //copy to clipboard
  document.execCommand("copy");
};

copyEmailAdress = () => {
  //get the text to copy
  var textToCopy = document.querySelector("#emailResult");
  //focus on the text box and select the text
  textToCopy.focus();
  textToCopy.select();
  //copy to clipboard
  document.execCommand("copy");
};

let phoneNumberCopyBtn = document.querySelector(".copyPhoneNumberBtn");
phoneNumberCopyBtn.addEventListener("click", copyPhoneNumber);

let emailAdressCopyBtn = document.querySelector(".copyEmailBtn");
emailAdressCopyBtn.addEventListener("click", copyEmailAdress);
