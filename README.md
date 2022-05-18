# sfomuseum-properties

What things mean in SFO Museum documents.

## Description

This repository contains machine-readable properties descriptions for properties in `sfomuseum-data/sfomuseum-data-*` repositories that are not already included in the [whosonfirst/whosonfirst-properties](https://github.com/whosonfirst/whosonfirst-properties) repository.

Some (but not all) of these properties may eventually be moved in to the `whosonfirst/properties` repository.

The records were created using the `index` tool which is part of the [whosonfirst/go-whosonfirst-properties](https://github.com/whosonfirst/go-whosonfirst-properties) package. For example:

```
$> ./bin/index \
	-exclude 'misc\:.*' \
	-alternate /usr/local/whosonfirst/whosonfirst-properties/properties \
	-properties /usr/local/sfomuseum/sfomuseum-properties/properties/ \
	/usr/local/data/sfomuseum-data-*
```

## See also

* https://github.com/whosonfirst/whosonfirst-properties
* https://github.com/whosonfirst/go-whosonfirst-properties