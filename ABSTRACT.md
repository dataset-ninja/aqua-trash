The authors released an open-source **AquaTrash Dataset** which consists of 369 images from 4 different categories related to various litter items. All the images in the AquaTrash dataset are manually annotated to obtain accuracy in the results. The dataset is based on the [TACO](http://tacodataset.org/) data set.

Note, similar **AquaTrash Dataset** dataset is also available on the [DatasetNinja.com](https://datasetninja.com/):

- [TACO](https://datasetninja.com/taco)

## Motivation

The escalating global pollution levels have emerged as a paramount concern for individuals, policymakers, and environmentalists alike. Substantial efforts are underway to mitigate air and water pollution, primarily driven by human activities. The pervasive impact of human-induced pollution is evident through the ubiquitous presence of waste across the planet, from remote regions like the Himalayas to vast expanses such as the Indian Ocean. Presently, the oceans are burdened with an estimated 5.25 trillion litter objects, a figure that continues to escalate daily. Among this staggering quantity of debris are numerous hazardous materials that pose significant threats to marine ecosystems. These pollutants encompass a range of harmful substances including plastics, bottles, chemical waste, and various toxic contaminants, contributing to widespread environmental degradation.

The adverse effects of marine pollution extend beyond environmental concerns, posing severe ramifications for small-scale economic activities reliant on marine resources. Alarmingly, it is estimated that approximately 90% of the world's fisheries have already been depleted, signaling a dire state of affairs. Projections indicate a concerning trajectory, with the anticipated ratio of fish to plastic waste projected to equalize at 1:1 by 2050, compared to 1:5 in 2014. This alarming trend underscores the urgent need for proactive measures to mitigate environmental degradation. Swift action is imperative to steer away from this perilous path and safeguard the integrity of our ecosystems, as it stands as an urgent imperative for the present moment.

## Dataset description

There are very few open-source datasets available which consist of a large number of garbage images and could be used for the proposed study. A comparative study has been done between the two available datasets – [TrashNet](https://github.com/garythung/trashnet) and [TACO](http://tacodataset.org/) dataset. Both the datasets have some shortcomings such as either the annotations were crowdsourced and unreliable or there were no annotations at all. So, the authors have proposed an other dataset AquaTrash to perform various experiments using the proposed AquaVision model. They have also released an open-source dataset AquaTrash which consists of 369 images from 4 different categories related to various litter items. All the images in the AquaTrash are manually annotated to obtain accuracy in the results. The AquaTrash dataset consists of 369 images from the [TACO](http://tacodataset.org/) dataset and represents manually annotated trash objects in each image. 

<img src="https://github.com/dataset-ninja/aqua-trash/assets/120389559/9687a049-d24a-43f3-92e6-39ed9b6f335c" alt="image" width="600">

<span style="font-size: smaller; font-style: italic;">A sample image from AquaTrash dataset with a yellow box as Ground Truth Label.</span>

| Parameters          | TrashNet [5] | TACO [6]      |
|---------------------|--------------|---------------|
| Number of Images    | 2527         | ~1500         |
| Number of Annotations | Labeled Data | ~4784         |
| Mode of annotation  | None         | Crowd-source  |
| Categories          | 6            | ~28 (excluding sub-categories) |
| Size                | ~3.5 GB      | ~2.63 GB      |
| Background          | Plain        | Random        |

<span style="font-size: smaller; font-style: italic;">A comparison of two open source Trash datasets available with proposed dataset.</span>

