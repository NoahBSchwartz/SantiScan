import wixData from 'wix-data';
import axios from 'axios';

$w.onReady(function () {
  axios.get('http://127.0.0.1:8080')
    .then(response => {
      const data = response.data;
      console.log(response.data);
      const items = [];

       wixData.query("tracker")
        .find()
        .then(results => {
          const toDelete = results.items.map(item => item._id);
          wixData.bulkRemove("tracker", toDelete)
            .then(() => {
              console.log("Items deleted successfully.");
            })
            .catch((error) => {
              console.error("Failed to delete items:", error);
            });
        })
        .catch((error) => {
          console.error("Failed to find items:", error);
        });

      // Extract the keys for Date, Time, and Name
      const dateKeys = Object.keys(data).filter(key => key.includes('Date'));
      const timeKeys = Object.keys(data).filter(key => key.includes('Time'));
      const nameKeys = Object.keys(data).filter(key => key.includes('Name'));

      // Loop through the keys and create an item for each entry
      for (let i = 0; i < dateKeys.length; i++) {
        const item = {
          date: data[dateKeys[i]],
          time: data[timeKeys[i]],
          name: data[nameKeys[i]]
        };
        items.push(item);
      }
      // Insert all items into the "tracker" collection
      wixData.bulkInsert("tracker", items)
        .then((result) => {
          console.log("Items inserted successfully:", result);
          $w("#table1").refresh();
          console.log("bruh");
        })
        .catch((error) => {
          console.error("Failed to insert items:", error);
        });
    });
});
