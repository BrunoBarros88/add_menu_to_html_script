const triggerBtn = document.querySelector('[example-attribute="EXAMPLE_HTML_ATTRIBUTE_VALUE"]');
const dropdownMenu = document.querySelector('.example-html-class');

triggerBtn.addEventListener('click', function () {
  if (dropdownMenu.classList.contains('show')) {
    dropdownMenu.classList.remove('show');
  } else {
    dropdownMenu.classList.add('show');
  }
});

triggerLink.addEventListener('click', function (e) {
  e.preventDefault();
  if (dropdownMenu.classList.contains('show')) {
    dropdownMenu.classList.remove('show');
  } else {
    dropdownMenu.classList.add('show');
  }
});