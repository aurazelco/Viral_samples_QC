# Viral Samples - QC

This Python script checks the sequencing quality of viral samples. 

## Cloning the repo

You can clone this repo by typing :
```
git clone https://github.com/aurazelco/Viral_samples_QC.git
```

## Using the script

To use the script, please type in the command line:
```
python python viral_samples_QC.py -i samples.txt
```

Where *python* is to call the script (you may have to use py or python3 instead), *viral_samples_QC.py* is the name of the script itself and *samples.txt* is where the file we want to analyze. 

## Limitations

Because of time constraints and some issues with the pandas module, the script is not running yet. However, below you can find the procedure which I have tried to implement, and how I would have progressed with more time. 

## Brief procedure and warnings

Using argparse, I make the file a required argument, so that the script has tp have an input before running. Also, I would have added a check on the file extension, so the user knows to always submit a txt or csv file. 

Once these checks are passed, I would have read the file into a pandas dataframe (which is the troubleshooting step at the moment), so that the data can be divided in the six columns. 

Once the dataframe is ready, I would have counted how many passed and not passed samples we have in the file, and print that number for the user. Finally, I would havwe counted how many samples were failed, and if 10% or more, I would have printed a warning for the user. Otherwise, a message saying that the samples can continue in the pipeline would have appeared. 


### Final comments

Unfortunately, because of the issues with my pandas module, the script is not running at the moment. However, the code itself should be working so that we get the QC pass and fail counts. With more time, I would have added a check for the input file extension, custom errors instead of just printing the message, and added an optional argument to save the results of the QC check in an output file, so for each file we get a mini report of this check without having to re-run the script. 