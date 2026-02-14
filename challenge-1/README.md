# Summary

In the first 3 scenario, grep was used to get to the result:
- regex to filter for HTTP requests (we only have http 1.0 and 2.0 in the .log file, but we could have also had 0.9, 1.1 or 3.0, hence the `[0-9.]*`) and the other condition(s);
- `-c` flag will print the number of lines that grep outputted, which allows us to only go through the list once.

In the 4th scenario we used `-v` flag to exclude matches.

In the 5th scenario, we used `sed` because the challenge said "replace". We could have also just summed up 503s and 500x.

# Count all lines with `500` HTTP code.

There are 714 lines with 500 HTTP code.

```
$ grep -c 'HTTP/[0-9.]* 500' sample.log
714
```

# Count all `GET` requests from `yoko` to `/rrhh` location and if it was successful (`200`).

The number of requests is 4.

```
$ grep -c 'yoko.*HTTP/[0-9.]* 200 "GET /rrhh"' sample.log
4
```

# How many requests go to `/`?

717 requests go to `/`

```
$ grep -c 'HTTP/.*"[A-Z]* /"' sample.log
717
```

# Count all lines _without_ `5XX` HTTP code.

2191 lines without `5xx` code.

```
$ grep -cv 'HTTP/[0-9.]* 5[0-9][0-9]' sample.log
2191
```

# Replace all `503` HTTP codes by `500`, how many requests have a `500` HTTP code?

1469 requests are either 503 or 500.

```
$ sed 's/HTTP\/\([0-9.]*\) 503/HTTP\/\1 500/' sample.log | grep -c 'HTTP/[0-9.]* 500'
1469
```
