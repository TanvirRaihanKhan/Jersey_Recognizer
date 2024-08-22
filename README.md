# Jersey_Recognizer
An image classification model from data collection,cleaning,model training,deployment and API integration <br/>
The model can classify different types of Football Club Jerseys of Europe's top 20 club  <br/>
They are following: <br/>
1. AC Milan Jersey
2. Arsenal Jersey
3. Atletico Madrid Jersey
4. Barcelona Jersey
5. Bayern Munich Jersey
6. Borussia Dortmund Jersey
7. Chelsea Jersey
8. FC Porto Jersey
9. Inter Milan Jersey
10. Juventus Jersey
11. Leeds United Jersey
12. Liverpool Jersey
13. Manchester City Jersey
14. Manchester United Jersey
15. Napoly Jersey
16. Newcastle Jersey
17. PSG Jersey
18. Real Madrid Jersey
19. Southampton Jersey
20. Tottenham Jersey

# Dataset preparation
**Data Collection:**Downloaded from DuckDuckGo using term name <br/>
**Dataloader:** Used fastai DataBlock API to set uo the DataLoader <br/>
**Data Augmentation:** fastai provides data augmentation which operates in GPU <br/>
Details can be found in 'notebooks\JerseyRecogniser_Data_collection.ipynb'
