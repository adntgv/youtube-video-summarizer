let url = ""; 

// on window content loaded
window.addEventListener("load", function () {
    // wait for 3 seconds
    setTimeout(function () {
        // add clickable icon to each video thumbnail by "ytd-thumbnail" tag
        const thumbnails = document.getElementsByTagName("ytd-thumbnail");
        const limit = thumbnails.length;
        for (let i = 0; i < limit; i++) {
            addTextOverlay(thumbnails[i]);
        }
    }, 3000);
});

function addTextOverlay(thumbnail) {
    const aTag = getATag(thumbnail)
    if (aTag === null) {
        return;
    }
    const videoId = getVideoId(aTag);
    if (videoId === null) {
        return;
    }

    const overlay = document.createElement("div");
    sendRequest(overlay, videoId);
    aTag.appendChild(overlay);
    aTag.addEventListener("mouseover", function () { 
        overlay.setAttribute("style", "position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-color: rgba(0, 0, 0, 0.8); color: white; display: flex; justify-content: center; align-items: center; font-size: 14px; overflow: auto;");
    });
    aTag.addEventListener("mouseout", function () {
        overlay.setAttribute("style", "display: none;");
    });
}

// Send a request to the external site
function sendRequest(el, videoId) {
    el.innerHTML = "Summarization in progress...";

    chrome.storage.local.get(['url', ], function (result) {
        url = result.url;

        const xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function () {
            if (xhr.readyState === 4) {
                if (xhr.status === 200) {
                    // on mouse hover
                    el.innerHTML = xhr.responseText;
                } else {
                    el.innerHTML = "Error: " + xhr.responseText;
                    console.log("Error: ", xhr.status, xhr.responseText);
                }
            }
        }

        const data = prepareData(videoId);
        console.log('Sending data', data)

        xhr.open("POST", url, true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.send(JSON.stringify(data));
    });
}
 

function prepareData(videoId) {
    let data = {
        id: videoId
    };
 
    return data;
}

function getVideoId(aTag) {
    if (aTag === null) {
        return;
    }

    href = aTag.getAttribute("href");
    if (href === null) {
        return;
    }

    // get video id from a tag
    return href.split("=")[1];
}

function getATag(thumbnail) {
    // iterate over children and find a tag
    var aTag = null;
    for (let j = 0; j < thumbnail.children.length; j++) {
        const child = thumbnail.children[j];
        if (child.tagName === "A") {
            aTag = child;
            break;
        }
    }

    return aTag;
}
