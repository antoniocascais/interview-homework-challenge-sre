# Summary

`myscript.py` returns the expected system information.

It supports passing multiple flags at the same time and outputs storage information in Megabytes (M) or Gigabytes (G).

Some try..catch added to make the script more robust when exceptions happen.
The `sleep(1)` was added because `Process.cpu_percent` needs to warm-up: first call always returns 0% CPU usage.

## Usage examples

### Single flags

```
$ python myscript.py -o
PID      CPU%     NAME
141428   7.8      dockerd
957358   5.8      Isolated Web Co
2379428  4.9      firefox
569280   2.9      apps.plugin
1253518  2.9      python
2375500  2.9      pipewire-pulse
2379866  2.9      Utility Process
3633302  2.9      Isolated Web Co
568932   1.9      netdata
2759979  1.9      Isolated Web Co
```

```
$ python myscript.py -d
/dev/mapper/luks-<REDACTED> (/): total=177.8G used=124.3G free=44.4G 73.7%
/dev/nvme0n1p1 (/mnt/docker_data): total=277.7G used=80.2G free=183.3G 30.4%
/dev/nvme0n1p6 (/boot/efi): total=998M used=0M free=997M 0.0%
```

```
$ python myscript.py -c
Cores: 10 physical, 12 logical
Usage: 6.6%
Frequency: 686MHz
```

```
$ python myscript.py -r
Total: 15.3G
Used: 10.2G
Free: 4.1G
Used: 73.2%
```

### Multiple flags

```
$ python myscript.py -rd
/dev/mapper/luks-<REDACTED> (/): total=177.8G used=124.3G free=44.4G 73.7%
/dev/nvme0n1p1 (/mnt/docker_data): total=277.7G used=80.2G free=183.3G 30.4%
/dev/nvme0n1p6 (/boot/efi): total=998M used=0M free=997M 0.0%
Total: 15.3G
Used: 10.2G
Free: 4.1G
Used: 73.0%
```
