async function x() {
    const searchTextArea = document.querySelector('.b_searchboxForm textarea');
    
    let text = await navigator.clipboard.readText()
    searchTextArea.value = text;

    // Dispatch an input event to ensure the value is updated in any listeners
    const inputEvent = new Event('input', { bubbles: true });
    searchTextArea.dispatchEvent(inputEvent);

    // Create and dispatch the Enter key press event
    const enterKeyEvent = new KeyboardEvent('keydown', {
        key: 'Enter',
        code: 'Enter',
        keyCode: 13,
        which: 13,
        bubbles: true,
        cancelable: true
    });
    searchTextArea.dispatchEvent(enterKeyEvent);
}
x()