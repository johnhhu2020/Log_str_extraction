# Log_str_extraction

here is how to use it:
say if you wat to extract the role_id and vip values from: 
    ole_occ":4,"role_id":"698382","vip":6,"pre_level":69,"gu
here is what you do in your bash:
    python3  Log_Ext.py "interview.log" "interview_processed.log"   "\"role_id\":\""  "\",\"vip\":"  "\",\"vip\":"  ",\"pre_level"
