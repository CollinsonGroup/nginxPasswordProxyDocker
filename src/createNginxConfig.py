#!/usr/bin/env python
import os
import sys
from quik import FileLoader

templateValues = {
    'destinationUrl': os.getenv('PASSTHRU_DESTINATION', 'http://localhost:8080')
}

# fill in template and save
def main(argv):
    baseFolder = '/etc/nginxTemplates'
    outputFilePath = "/etc/nginx/nginx.conf"

    # Format template with values from environment
    loader = FileLoader(baseFolder)
    template = loader.load_template('nginx.conf.tmpl')
    renderedTemplate = template.render(templateValues,
                          loader=loader).encode('utf-8')

    # Save into logstash folder
    with open(outputFilePath, "w") as text_file:
        text_file.write("{0}".format(renderedTemplate))

if __name__ == "__main__":
   main(sys.argv[1:])
