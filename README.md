# sfomuseum-properties

What things mean in SFO Museum documents.

## Description

This repository contains machine-readable properties descriptions for properties in `sfomuseum-data/sfomuseum-data-*` repositories that are not already included in the [whosonfirst/whosonfirst-properties](https://github.com/whosonfirst/whosonfirst-properties) repository.

Some (but not all) of these properties may eventually be moved in to the `whosonfirst/properties` repository.

The records were created using the `index-properties` tool which is part of the [whosonfirst/go-whosonfirst-properties](https://github.com/whosonfirst/go-whosonfirst-properties) package. For example:

```
> ./bin/index-properties \
	-iterator-uri org:///tmp \
	-properties /usr/local/sfomuseum/sfomuseum-properties/properties \
	-alternate /usr/local/whosonfirst/whosonfirst-properties/properties \
	'sfomuseum-data://?prefix=sfomuseum-data-&exclude=sfomuseum-data-flights-YYYY-MM'
```

## See also

* https://github.com/whosonfirst/whosonfirst-properties
* https://github.com/whosonfirst/go-whosonfirst-properties