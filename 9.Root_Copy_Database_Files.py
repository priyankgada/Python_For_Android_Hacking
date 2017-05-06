import subprocess #for importing sub processes 

proc =  subprocess.Popen('su',  stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)#takes superuser access and sends command in pipe

command = 'cp /data/data/com.whatsapp/databases/wa.db /storage/emulated/0/' +\#copywa.db file to root of sd card
          ' ; cp /data/data/com.whatsapp/databases/msgstore.db /storage/emulated/0/'+\#copy msgstore.db file to root of sdcard
          ' ; cp /data/data/com.sec.android.provider.logsprovider/databases/logs.db /storage/emulated/0/'#copy logs.db file to root of sdcard
(out, err) = proc.communicate(command)
#subscribe www.youtube.com/priyankgada















