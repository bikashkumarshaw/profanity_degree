# profanity_degree

#### The program takes a txt tweet file that has paragraphs in each line and a slur file that would contain slur words in each line.
It return the degree of profanity of each sentences in each line.

### Run command:

```
python profanity.py --tweet-file tweet.txt --profanity-file default_slur.txt
```

Note specifying profanity-file  in the run command is not mandatory, if this argument is not provided then by default default_slur.txt file is chosen.

Eg.

```
python profanity.py --tweet-file tweet.txt
```
