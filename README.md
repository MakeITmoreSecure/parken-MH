This project aims to showcase the bad security on the parken-mh API / endpoints.
Actually this allows me to track my friends & family across the city.

# Track_Me
this can be used to track a single plate 
```shell
python3 code/track_me.py --plate M-AS213
```

a [] means, nothing found, the rest will explain itself :D 


# Brute me
```shell
 python3 code/track_brute.py -c M -l UC -s 100 -e 999
```
this will test all plates starting:
```text
MUC100
MUC101
...
MUC998
MUC999
```