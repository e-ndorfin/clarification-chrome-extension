// A generic onclick callback function.
chrome.contextMenus.onClicked.addListener(function (info) { // Listens for context menu click
    const text = info.selectionText; // gets selected text 
    chrome.windows.create({ // creates window, with data of context passed as variable
        url: "http://127.0.0.1:5000/?text=" + text, 
        type: "popup", 
        height: 650, 
        width: 500})
});

// What info returns: 
// editable: false
// frameId: 0
// frameUrl: "chrome://extensions/"
// menuItemId: "selection"
// pageUrl: "chrome://extensions/"
// selectionText: "quiz"


chrome.runtime.onInstalled.addListener(function () { // creates context menu 
    chrome.contextMenus.create({
        title: "Quiz me!",
        contexts: ["selection"],
        id: "selection"
      });
    }); 