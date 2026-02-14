# Summary

The helm chart was copied over from challenge 5 and tests were added.
They pass, as expected.

```
$ cp -R challenge-5/server-chart/ challenge-extra-3/
$ ls challenge-extra-3/server-chart/
Chart.yaml  templates  values.yaml
```

```
$ helm unittest server-chart

### Chart [ server-chart ] server-chart

 PASS  test deployment	server-chart/tests/deployment_test.yaml
 PASS  test service	server-chart/tests/service_test.yaml

Charts:      1 passed, 1 total
Test Suites: 2 passed, 2 total
Tests:       16 passed, 16 total
Snapshot:    0 passed, 0 total
Time:        11.293226ms
```

## Considerations

The unit tests are kinda simple: they test that the expected resources are created, also test that they have the expected properties and that changing values actually works.

For this use-case, this should be enough.
