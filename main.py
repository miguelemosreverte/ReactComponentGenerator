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


def imports(component_name, props, component_type):
    return \
        """ 
        import React,{ """ + component_type + """ } from 'react';
        import styles from './""" + component_name + """.scss';
        import classNames from 'classnames/bind';
        """ \
    +   f"""
        {"import PropTypes from 'prop-types';" if props else ""}
        """ \
    +   """
        const cx = classNames.bind(styles);
        """


def stateless(component_name, props, class_name, component_type):
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

def component(component_name, props, class_name, component_type):
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


def prop_types_and_export(component_name, props, prop_types):
    return \
        f"""
        {prop_types if props else ""}
        """ \
    +   f"""
        export default {component_name};
        """


def create_class_component(
    component_name
    , class_name
    , props
    , prop_types
    , component_type
): return create_template(
    header=imports(component_name, props, component_type)
    , body=component(component_name, props, class_name, component_type)
    , footer=prop_types_and_export(component_name, props, prop_types)
)


def create_pure_component(
        component_name
        , class_name
        , props
        , prop_types
):
    component_type = "PureComponent"
    return \
    create_template(
          header=imports(component_name, props, component_type)
        , body=component(component_name, props, class_name, component_type)
        , footer=prop_types_and_export(component_name, props, prop_types)
    )

def create_standard_component(
        component_name
        , class_name
        , props
        , prop_types
):
    component_type = "Component"
    return \
    create_template(
          header=imports(component_name, props, component_type)
        , body=component(component_name, props, class_name, component_type)
        , footer=prop_types_and_export(component_name, props, prop_types)
    )

def create_stateless_component(
        component_name
        , class_name
        , props
        , prop_types
):
    component_type = "Component"
    return \
    create_template(
          header=imports(component_name, props, component_type)
        , body=stateless(component_name, props, class_name, component_type)
        , footer=prop_types_and_export(component_name, props, prop_types)
    )

def create_component(
        component_name
        , class_name
        , props
        , prop_types
): return create_class_component(
    component_name=component_name
    , class_name=class_name
    , props=props
    , prop_types=prop_types
    , component_type="Component"
)


output = create_stateless_component(
    component_name="HERE_GOES_componentName"
    , class_name="HERE_GOES_className"
    , props="HERE_GOES_props"
    , prop_types="HERE_GOES_proptypes"
)
print(output)
