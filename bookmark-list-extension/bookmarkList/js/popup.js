// Retrieve bookmarks and display them in the popup
chrome.bookmarks.getTree(function (bookmarksTree) {
    const bookmarkList = document.getElementById('bookmarkList');

    function processNode(node) {
        if (node.children) {
            //const folderItem = document.createElement('li');
            //folderItem.textContent = node.title;
            //const folderList = document.createElement('ul');
            //const folderList = document.createElement('ul');
            node.children.forEach(processNode);
            folderItem.appendChild(folderList);
            bookmarkList.appendChild(folderItem);
        } else if (node.url) {
            const bookmarkItem = document.createElement('li');
            bookmarkItem.className = 'bookmark-item';
            const bookmarkLink = document.createElement('a');
            bookmarkLink.className = 'bookmark-link';
            bookmarkLink.textContent = node.title;
            bookmarkLink.href = node.url;
            bookmarkItem.appendChild(bookmarkLink);
            bookmarkList.appendChild(bookmarkItem);

            // Abre o link em uma nova TAB
            bookmarkLink.target = '_blank';
            
            bookmarkItem.appendChild(bookmarkLink);
            bookmarkList.appendChild(bookmarkItem);
        }
    }

    bookmarksTree.forEach(processNode);
});
