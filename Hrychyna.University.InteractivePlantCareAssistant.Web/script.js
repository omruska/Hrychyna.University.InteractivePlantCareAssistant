let currentThread = null;

function addThread() {
    var input = document.getElementById('newThreadTitle');
    var threadTitle = input.value.trim();
    if (threadTitle === "") {
        alert("Please enter a topic name.");
        return;
    }

    var threadsList = document.getElementById('threadsList');
    var li = document.createElement('li');

    var userName = "Dariia";
    var currentTime = new Date().toLocaleString("uk-UA");

    li.innerHTML = `<span class="thread-title">${threadTitle}</span> <span class="thread-info">(Created by ${userName} at ${currentTime})</span>
        <span class="likes" onclick="toggleLike(this)">
            <svg class="heart" viewBox="0 0 32 29.6">
                <path d="M23.6,0A8.6,8.6,0,0,1,32,8.6c0,9.1-14.4,21-16,21S0,17.7,0,8.6A8.6,8.6,0,0,1,8.6,0a9.3,9.3,0,0,1,7.4,3.6A9.3,9.3,0,0,1,23.6,0Z"/>
            </svg>
            <span class="like-count">0</span>
        </span>`;

    li.onclick = function(event) {
        if (event.target.closest('.likes')) return;
        openThread(threadTitle);
    };

    threadsList.appendChild(li);
    input.value = "";
}



function incrementLikes(element) {
    var likeCount = element.querySelector('.like-count');
    var count = parseInt(likeCount.textContent, 10);
    likeCount.textContent = count + 1;
    element.classList.toggle('liked');
}

function toggleLike(element) {
    const likeCountSpan = element.querySelector('.like-count');
    let likes = parseInt(likeCountSpan.textContent, 10);
    
    if (element.classList.contains('liked')) {
        // If already liked, decrease the like count and change color to default
        likes--;
        element.classList.remove('liked');
    } else {
        // If not liked, increase the like count and change color to red
        likes++;
        element.classList.add('liked');
    }

    likeCountSpan.textContent = likes; // Update the display of likes
}




function openThread(title) {
    currentThread = title;
    document.getElementById('threadTitle').textContent = 'Topic: ' + title;
    document.getElementById('threadsView').style.display = 'none';
    document.getElementById('messagesView').style.display = 'block';
    document.getElementById('messagesList').innerHTML = '';  // Очистити повідомлення
}



function addMessage() {
    var input = document.getElementById('newMessageText');
    var messageText = input.value.trim();
    if (messageText === "") {
        alert("Please enter a text message.");
        return;
    }

    var messagesList = document.getElementById('messagesList');
    var li = document.createElement('li');
    li.classList.add('message-item');  // Added class for flex layout
    li.innerHTML = `<span class="message-text">${messageText}</span>
        <span class="message-likes" onclick="toggleMessageLike(this)">
            <svg class="heart" viewBox="0 0 32 29.6">
                <path d="M23.6,0A8.6,8.6,0,0,1,32,8.6c0,9.1-14.4,21-16,21S0,17.7,0,8.6A8.6,8.6,0,0,1,8.6,0a9.3,9.3,0,0,1,7.4,3.6A9.3,9.3,0,0,1,23.6,0Z"/>
            </svg>
            <span class="like-count">0</span>
        </span>`;
    
    messagesList.appendChild(li);
    input.value = ""; // Clear input field after adding
}


function toggleMessageLike(element) {
    const likeCountSpan = element.querySelector('.like-count');
    let likes = parseInt(likeCountSpan.textContent, 10);
    
    if (element.classList.contains('liked')) {
        // Decrease the like count and change color to default
        likes--;
        element.classList.remove('liked');
    } else {
        // Increase the like count and change color to red
        likes++;
        element.classList.add('liked');
    }

    likeCountSpan.textContent = likes; // Update the display of likes
}





function goBack() {
    document.getElementById('threadsView').style.display = 'block';
    document.getElementById('messagesView').style.display = 'none';
}

document.getElementById('newThreadTitle').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        addThread();
    }
});

document.getElementById('newMessageText').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
        addMessage();
    }
});
