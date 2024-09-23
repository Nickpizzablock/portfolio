// In quicklinks.html
// if user ctrl+k, then override the browser shortcut and put cursor on form input
document.addEventListener('keydown', function(event) {
    if (event.ctrlKey && event.key === 'k') {
        event.preventDefault();
        console.log('Ctrl + k was pressed');
        const input = document.querySelector('input');
        input.value = '';
        input.focus();
    }
});

// make a dictionary of links from links.csv
const links = {};

document.addEventListener('DOMContentLoaded', function() {
    console.log(links);

    // Listen for user input
    const input = document.querySelector('input');
    document.addEventListener('keydown', function(event) {
        // console.log('Key pressed:', event.key);
        if (event.key === 'Enter') {
            event.preventDefault()
            const name = input.value;
            const url = links[name];
            // console.log('Entered name:', name, 'Link:', links[name]);
            if (url) {
                window.location.href = url;
            } 
        }
    });
});

// Assuming links.csv is a CSV file with two columns: name and url
fetch('links.csv')
    .then(response => response.text())
    .then(data => {
        const rows = data.split('\n').filter(row => row.trim() !== '');
        rows.forEach(row => {
            const [category, name, url] = row.split(',');
            // name = name.trim();
            // url = url.trim();
            // console.log('name:', name, 'url:', url);
            // links[name] = url;
            links[name.trim()] = url.trim();
        });
    })
    .catch(error => {
        console.error('Error fetching links:', error);
    });




