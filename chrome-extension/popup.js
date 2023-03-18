document.addEventListener("DOMContentLoaded", function () {
    // get token and userPrompt from storage
    let url = null;
    chrome.storage.local.get(['url'], function (result) {
        url = result.url;
    });

    document.getElementById('url').value = url; 

    document.getElementById('form').addEventListener('submit', function (event) {
        event.preventDefault();
        // get token and userPrompt from storage 

        const url = document.getElementById('url').value;
        
        chrome.storage.local.set({ url }, function () {
            console.log('Settings saved');
            document.getElementById('saveResult').innerHTML = 'API url set to: ' + url + '';
            //refresh chrome tab
            chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
                chrome.tabs.reload(tabs[0].id);
            });
        })
    });
});