maintenance
==

zipfolder.py
--

example:

```
40 23 * * * /root/.script/zipfolder.py /docker/ /home/backup/docker-container
```

this task will zip up all the folders in ```/docker/``` ,  and put the *.zip file into the destination folder ``` /home/backup/docker-container/ ```, additionally, it also create a folder using today's date '%Y-%m-%d' , and the *.zip archives will be sorted in these folders.

the archive looks like this:

```
/home/backup/docker-container/
└── 2018-10-10
    ├── lims03000026-2018-10-10_112225.zip
    ├── lims16000025-2018-10-10_112225.zip
	...
    ├── lims99000018-2018-10-10_112225.zip
    └── lims99000024-2018-10-10_112225.zip

```	

deloldfile.py
--

example:

```
10 23 * * * /root/.script/deloldfile.py  /home/backup/lims_st/  30 -r
```

As you have backed-up you folders day by day,   the disk will be feed-up someday, sooner or later.
so you have to remove some of the old archives created before a certain date.

in this example, the script will remove the *.zip file older than 30 days.  the -r switch means traval the folder recursively.
