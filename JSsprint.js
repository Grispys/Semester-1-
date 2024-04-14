// Desc - detail log for upcoming video games
// Auth - Matthew Verge
// Date - 28/03/2024

// my program will be about the release date and prices of various upcoming games.
// containing their title, price, release date. print to both console
// and html
document.addEventListener("DOMContentLoaded", function() {

    // parse and store json + html
    fetch(`./info.json`)
        .then(response => response.json())
        .then(gINfo => {
            let gamesWEB = '';

            // here is my forEach loop that iterates over each record
            gINfo.forEach(game => {
                const gameWEB = `
                <div>
                    <h4>${game.title} 
                    &nbsp&nbsp-&nbsp&nbsp&nbspCST: $${game.price}
                    &nbsp&nbsp&nbsp-&nbsp&nbsp&nbsp REL: ${game.release}  </h4>
                    </br>
                </div>
                `
                gamesWEB += gameWEB;
            });

            // this const is outside the forEach so that after the full content of each game is displayed, this doesn't get repeated.
            const gameRAW = `
            <div>
            ${getTitles(gINfo)}</br></br>
            ${getPrices(gINfo)}</br></br>
            ${getRelease(gINfo)}</br></br>
            </div>
            `
            gamesWEB += gameRAW;

            // here are my functions that will grab the content from specific portions of the json to display in the console
            
            function getTitles(games) {
                const titles = games.map(game => game.title);
                return `GAME TITLES: ` + titles.join(", ");
            }
            
            function getPrices(games) {
                const prices = games.map(game => game.price);
                return `GAME PRICES: ` + prices.join(", ");
            }
            
            function getRelease(games) {
                const dates = games.map(game => game.release);
                return `RELEASE DATES: ` + dates.join(", ");
            }

            document.body.innerHTML = gamesWEB;
            console.log(getTitles(gINfo));
            console.log(getPrices(gINfo));
            console.log(getRelease(gINfo))
        })


        // catch errors waaaaaa
    .catch(error => console.error(`there was an error fetching something.`, error));

  
});

