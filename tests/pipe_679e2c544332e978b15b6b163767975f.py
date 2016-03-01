# -*- coding: utf-8 -*-
# vim: sw=4:ts=4:expandtab
# Pipe pipe_679e2c544332e978b15b6b163767975f generated by pipe2py

from pipe2py import Context
from pipe2py.modules import pipeitembuilder, pipestrreplace


def pipe_679e2c544332e978b15b6b163767975f(item=None, context=None, conf=None, **kwargs):
    if context and context.describe_input:
        return []

    if context and context.describe_dependencies:
        return ['pipeitembuilder', 'pipestrreplace']

    sw_232 = pipeitembuilder.pipe(
        item,
        context=context,
        conf={
            'attrs': [
                {
                    'value': {'type': 'text', 'value': 'www.google.com'},
                    'key': {'type': 'text', 'value': 'link'}
                }, {
                    'value': {'type': 'text', 'value': 'google'},
                    'key': {'type': 'text', 'value': 'title'}
                }, {
                    'value': {'type': 'text', 'value': '$'},
                    'key': {'type': 'text', 'value': 'author'}}]},
        **kwargs)

    sw_421 = pipestrreplace.pipe
    sw_421_conf = {
        'with': {'type': 'text', 'value': 'author'},
        'rule': [
            {
                'find': {'type': 'text', 'value': '$'},
                'param': {'type': 'text', 'value': 'first'},
                'replace': {'type': 'text', 'value': 'USD'}}]}


    output = (sw_421(i, context=context, conf=sw_421_conf, **kwargs) for i in sw_232)
    return output


if __name__ == "__main__":
    for i in pipe_679e2c544332e978b15b6b163767975f(Context()):
        print i
