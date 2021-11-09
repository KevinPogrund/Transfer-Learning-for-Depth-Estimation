# Transfer-Learning-for-Depth-Estimation
Final year research project into the efficacy of transfer learning for depth estimation in unstructured environments

## Investigation
Three State of the art depth networks were chosen and analyzed in the following phases. These depth network were:
- [AdaBins](https://github.com/shariqfarooq123/AdaBins)
- [LapDepth](https://github.com/tjqansthd/LapDepth-release)
- [BTS](https://github.com/cogaplex-bts/bts) 

### Evaluation
The first stage of the investigation was to evaluate how well the depth networks perfomed on the unstructured dataset. This was done both qualitatively and quantitatively. The quantitative evaluation was done within each dataset. In order to ensure an accurate qualitative comparison, all teh output images were converted to a 'jet' style depth map. This was done using [this](https://github.com/KevinPogrund/Transfer-Learning-for-Depth-Estimation/blob/main/to_jet.py) script.

### Adaption
The networks then had to be adapted to the unstructured dataset by using transfer learning. This is the code insterted into [BTS](https://github.com/KevinPogrund/Transfer-Learning-for-Depth-Estimation/blob/main/TL_BTS.py) and [LapDepth](https://github.com/KevinPogrund/Transfer-Learning-for-Depth-Estimation/blob/main/TL_LapDepth.py). AdaBins already implements transfer learning so the only adaptions needed was to set the correct height and width, for all three depth networks.

### Re-Evaluation
These networks, no trained on the unstructured data were then evaluated and the results were compared to eachother as well as to before and after training. 

### Results
