#!/usr/bin/env python

import os
import sys
import logging
import json

import mapzen.whosonfirst.utils

if __name__ == "__main__":

    import optparse
    opt_parser = optparse.OptionParser()

    opt_parser.add_option('-v', '--verbose', dest='verbose', action='store_true', default=False, help='Be chatty (default is false)')
    options, args = opt_parser.parse_args()

    if options.verbose:	
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    whoami = os.path.abspath(sys.argv[0])
    utils = os.path.dirname(whoami)
    root = os.path.dirname(utils)

    props = os.path.join(root, "properties")
    sfom_props = os.path.join(props, "sfomuseum")
    
    for repo in args:

        repo = os.path.abspath(repo)
        data = os.path.join(repo, "data")

        crawl = mapzen.whosonfirst.utils.crawl(data, inflate=True)

        for feature in crawl:

            props = feature["properties"]

            for k, v in props.items():

                if not k.startswith("sfomuseum:"):
                    continue

                k = k.split(":")
                k = k[1]

                fname = "%s.json" % k
                path = os.path.join(sfom_props, fname)

                if os.path.exists(path):
                    continue

                id = mapzen.whosonfirst.utils.generate_id()
                
                prop = {
                    "id": id,
                    "name": k,
                    "prefix": "sfomuseum",
                    "description": "",
                    "type": "string"
                }

                fh = open(path, "w")
                json.dump(prop, fh, indent=2)
                fh.close()

                logging.info("wrote %s", path)
                
                
