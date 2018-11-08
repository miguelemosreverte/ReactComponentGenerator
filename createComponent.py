def create_template(header, body, footer):
    '''
    This is a multiline comment.

    In the following function, you'll see multiline strings
    put to good use, alongside with the f-string, a way to
    easily interpolate strings in Python v3.
    '''
    return \
        f""" 
        {header}
        """ \
    +   f""" 
        {body}
        """ \
    +   f""" 
        {footer}
        """


def imports(param):
    '''
    Here we use both dict.get('key name') as dict['key name']

    dict.get('key name') is used to maybe find a value, can return None

    dict['key name'] is made under the assumption that the key exist.
    dict['key name'] will runtime exception if the key is not found.
    '''
    component_type = param.get("component_type") # key may not exist
    component_name = param["component_name"]
    props = param["props"]
    deestructuring = ",{"+component_type+"}" if component_type else ""
    return \
        """ 
        import React""" + deestructuring + """ } from 'react';
        import styles from './""" + component_name + """.scss';
        import classNames from 'classnames/bind';
        """ \
    +   f"""
        {"import PropTypes from 'prop-types';" if props else ""}
        """ \
    +   """
        const cx = classNames.bind(styles);
        """


def stateless(param):
    class_name = param["class_name"]
    component_name = param["component_name"]
    props = param["props"]
    '''
    Here we see triple braces in use:
    Two of them together represent a single brace not used for interpolation sintax.
    The third is indeed used for interpolation, and we use it to place out props variable.
    '''
    return \
        (f"const {component_name} = (" + f'{"{"+props+"}" if props else ""}') + ") => "\
    +   f"""(
            <div className={{cx('{class_name}')}}>
    
            </div>
        );"""

def component(param):
    class_name = param["class_name"]
    component_name = param["component_name"]
    component_type = param["component_type"]
    props = param["props"]
    return \
        """
    
        class """ + component_name + " extends " + component_type + """ {
        
            constructor(props) {
                super(props);
                this.state = { 
                    
                };
        
            }
        
            componentDidMount(){
        
            }
            
            render() { 
        """ \
   +    f"""
        {"            const {{" + props + "}} = this.props;" if props else ""}
        """ \
   +    """
                       return (
                           <div class_name={cx('""" + f"{class_name}" + """')}>
        
                    </div>
                );
            }
        }
        
        """


def prop_types_and_export(param):
    component_name = param["component_name"]
    props = param["props"]
    prop_types = param["prop_types"]
    return \
        f"""
        {prop_types if props else ""}
        """ \
    +   f"""
        export default {component_name};
        """


def create_class_component(param):
    return \
    create_template(
    header=imports(param)
    , body=component(param)
    , footer=prop_types_and_export(param)
)


def create_pure_component(param):
    param["component_type"] = "PureComponent"
    return \
    create_template(
          header=imports(param)
        , body=component(param)
        , footer=prop_types_and_export(param)
    )

def create_standard_component(param):
    param["component_type"] = "Component"
    return \
    create_template(
          header=imports(param)
        , body=component(param)
        , footer=prop_types_and_export(param)
    )

def create_stateless_component(param):
    return \
    create_template(
          header=imports(param)
        , body=stateless(param)
        , footer=prop_types_and_export(param)
    )



output = create_stateless_component({
      'component_name': "HERE_GOES_componentName"
    , 'class_name':     "HERE_GOES_className"
    , 'props':          "HERE_GOES_props"
    , 'prop_types':     "HERE_GOES_proptypes"
})
print(output)
