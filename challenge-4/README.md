# Summary

The binary needed `the_magic_filez.txt` to exist.

```
$ touch the_magic_filez.txt && ./blackbox
Congrats! :)
```

## How did I figure it out

Running `./blackbox` indeed failed:
```
$ ./blackbox
Ooooh, what's wrong? :(
```

Then running `strace` showed the problem:
```
$ strace ./blackbox
execve("./blackbox", ["./blackbox"], 0x7ffe48d41a00 /* 79 vars */) = 0
brk(NULL)                               = 0x55f623bc6000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=185359, ...}) = 0
mmap(NULL, 185359, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7fe3429bd000
close(3)                                = 0
openat(AT_FDCWD, "/usr/lib/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\360w\2\0\0\0\0\0"..., 832) = 832
pread64(3, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 896, 64) = 896
fstat(3, {st_mode=S_IFREG|0755, st_size=2145632, ...}) = 0
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7fe3429bb000
pread64(3, "\6\0\0\0\4\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0@\0\0\0\0\0\0\0"..., 896, 64) = 896
mmap(NULL, 2169904, PROT_READ, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7fe342600000
mmap(0x7fe342624000, 1511424, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x24000) = 0x7fe342624000
mmap(0x7fe342795000, 454656, PROT_READ, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x195000) = 0x7fe342795000
mmap(0x7fe342804000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x203000) = 0x7fe342804000
mmap(0x7fe34280a000, 31792, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7fe34280a000
close(3)                                = 0
mmap(NULL, 12288, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7fe3429b8000
arch_prctl(ARCH_SET_FS, 0x7fe3429b8740) = 0
set_tid_address(0x7fe3429b8a10)         = 1541764
set_robust_list(0x7fe3429b8a20, 24)     = 0
rseq(0x7fe3429b8680, 0x20, 0, 0x53053053) = 0
mprotect(0x7fe342804000, 16384, PROT_READ) = 0
mprotect(0x55f620e4e000, 4096, PROT_READ) = 0
mprotect(0x7fe342a24000, 8192, PROT_READ) = 0
prlimit64(0, RLIMIT_STACK, NULL, {rlim_cur=8192*1024, rlim_max=RLIM64_INFINITY}) = 0
getrandom("\x1d\xe7\x14\x7f\xe7\xf2\x9e\xa0", 8, GRND_NONBLOCK) = 8
munmap(0x7fe3429bd000, 185359)          = 0
access("the_magic_filez.txt", F_OK)     = -1 ENOENT (No such file or directory)
fstat(1, {st_mode=S_IFCHR|0600, st_rdev=makedev(0x88, 0x2b), ...}) = 0
brk(NULL)                               = 0x55f623bc6000
brk(0x55f623be7000)                     = 0x55f623be7000
write(1, "Ooooh, what's wrong? :(", 23Ooooh, what's wrong? :() = 23
exit_group(-1)                          = ?
+++ exited with 255 +++
```

Notice the `access("the_magic_filez.txt", F_OK)     = -1 ENOENT (No such file or directory)` line.

Creating the file and running the script again confirmed it was indeed the magic file :)

```
$ touch the_magic_filez.txt && strace ./blackbox
execve("./blackbox", ["./blackbox"], 0x7ffdeeb01080 /* 79 vars */) = 0
brk(NULL)                               = 0x55bfb7c02000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
...
access("the_magic_filez.txt", F_OK)     = 0
fstat(1, {st_mode=S_IFCHR|0600, st_rdev=makedev(0x88, 0x2b), ...}) = 0
brk(NULL)                               = 0x55bfb7c02000
brk(0x55bfb7c23000)                     = 0x55bfb7c23000
write(1, "Congrats! :)", 12Congrats! :))            = 12
exit_group(0)                           = ?
+++ exited with 0 +++
```
