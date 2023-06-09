const express = require('express');
const axios = require('axios');
const cheerio = require('cheerio');

const app = express();
const port = process.env.PORT || 3330;

app.get('/:num', async (req, res) => {
  try {
    const { num } = req.params;
    const { data } = await axios.get(`https://www.confirmtkt.com/train-running-status/${num}`);
    const modifiedData = modifyJSON(data);
    res.json(modifiedData);
  } catch (error) {
    console.error(error);
    res.status(500).send('Error occurred');
  }
});

app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});

function modifyJSON(data) {
  const $ = cheerio.load(data);

  const modifiedData = {
    trainName: $('title').text(),
    station: $('.circle.blink').next('.rs__station-name').map((index, element) => $(element).text()).get(),
    time: $('.circle.blink').parent().nextAll('.col-xs-2').map((index, element) => $(element).text().trim()).get().join(' ')
  };

  return modifiedData;
}
