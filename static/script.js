
function fetchEvents() {
    fetch('/events')
      .then(res => res.json())
      .then(data => {
        const container = document.getElementById('events');
        container.innerHTML = '';
  
        data.forEach(event => {
          const card = document.createElement('div');
          card.className = 'event-card';
  
          let message = '';
          const time = new Date(event.timestamp).toUTCString();
  
          if (event.action === "PUSH") {
            message = `${event.author} pushed to ${event.to_branch} on ${time}`;
          } else if (event.action === "PULL_REQUEST") {
            message = `${event.author} submitted a pull request from ${event.from_branch} to ${event.to_branch} on ${time}`;
          } else if (event.action === "MERGE") {
            message = `${event.author} merged branch ${event.from_branch} to ${event.to_branch} on ${time}`;
          }
  
          card.textContent = message;
          container.appendChild(card);
        });
      });
  }
  
  setInterval(fetchEvents, 15000);
  fetchEvents();
  
