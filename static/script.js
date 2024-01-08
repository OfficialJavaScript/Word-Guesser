document.addEventListener('keydown', function (event) {
    const activeElement = document.activeElement;

    if (event.key === 'Backspace' || event.keyCode === 8) {
        event.preventDefault(); // Prevent the default behavior of the Backspace key

        if (activeElement.tagName === 'INPUT') {
            const prevInputBox = activeElement.previousElementSibling;

            if (activeElement.value !== '') {
                activeElement.value = '';
            } else if (prevInputBox) {
                prevInputBox.focus();
            }
        }
    } else if (/^[a-zA-Z]$/.test(event.key) && activeElement.tagName === 'INPUT') {
        event.preventDefault(); // Prevent the default behavior of character keys

        activeElement.value = event.key;
        
        const nextInputBox = activeElement.nextElementSibling;

        if (nextInputBox) {
            nextInputBox.focus();
        }
    } else if (event.key === 'Enter') {
        // Allow Enter key to propagate
    } else {
        event.preventDefault(); // Prevent entering characters other than letters
    }
});
