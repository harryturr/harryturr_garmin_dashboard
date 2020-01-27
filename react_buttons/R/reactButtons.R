# AUTO GENERATED FILE - DO NOT EDIT

reactButtons <- function(test_text=NULL, id=NULL, label=NULL, value=NULL) {
    
    props <- list(test_text=test_text, id=id, label=label, value=value)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ReactButtons',
        namespace = 'react_buttons',
        propNames = c('test_text', 'id', 'label', 'value'),
        package = 'reactButtons'
        )

    structure(component, class = c('dash_component', 'list'))
}
