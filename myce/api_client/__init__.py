import os
import ramlfications
import requests
from config2.config import config

def create():
    api = ramlfications.parse(os.path.dirname(__file__) + "/../raml/myce.raml")
    return APIClient(api)

class APIClientNode():
    def  __init__(self):
        return None

    def get_client_node(self, node_path):
        if (len(node_path) > 1):
            if (node_path[0] not in self.__dir__()):
                setattr(self, node_path[0], APIClientNode())
            return getattr(self, node_path[0]).get_client_node(node_path[:1])
        else:
            return self

class APIClient(APIClientNode):
    def __init__(self, api):
        self.__build_client(api)
        
    def __build_client(self, api):
        for resource in api.resources:
            node_path = resource.raw[resource.method]['(client_name)'].split('.')
            client_node = self.get_client_node(node_path)
            resource_function = self.__build_resource_function(resource);

            setattr(client_node, node_path[-1], resource_function)

    def __build_resource_function(self, resource):
        implementer = resource.raw[resource.method]['(implementer)']
        base_uri = '%s:%s'%(config[implementer]['domain'], config[implementer]['port'])
        uri_params = resource.uri_params

        # as a side effect, this function removes uri params from the params object
        def interpolatePath(path, params):
            if uri_params is not None:
                for uri_param in uri_params:
                    path = path.replace('{%s}' %uri_param.name, params[uri_param.name])
                    del params[uri_param.name]

            return path
                
        def f(**kwargs):
            interpolated_uri = 'http://' + base_uri + interpolatePath(resource.path, kwargs)
            http_method = getattr(requests, resource.method)

            if http_method is 'get':
                return http_method(interpolated_uri)
            elif http_method is 'post':
                return http_method(interpolated_uri, json=kwargs)

        return f




