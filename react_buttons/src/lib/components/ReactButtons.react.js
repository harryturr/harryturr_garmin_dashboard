import React, {Component} from 'react';
import PropTypes from 'prop-types';
import ButtonGroup from '@material-ui/core/ButtonGroup';
import Button from '@material-ui/core/Button';

/**
 * ExampleComponent is an example component.
 * It takes a property, `label`, and
 * displays it.
 * It renders an input with the property `value`
 * which is editable by the user.
 */
export default class ReactButtons extends Component {
    render() {
        const {test_text, id, label, setProps, value} = this.props;

        return (
            <div id={id}>
               <ButtonGroup>
                <Button variant="contained" color="primary"
                    
                    onClick={e =>
                        setProps({
                            test_text: "04,11"
                        })
                    }              
                >
                all time    
                </Button>
 
                <Button variant="contained" color="default"
                    
                    onClick={e =>
                        setProps({
                            test_text: "08,11"
                        })
                    }              
                >
                3 months    
                </Button>

                <Button variant="contained" color="secondary"
                    
                    onClick={e =>
                        setProps({
                            test_text: "10,11"
                        })
                    }              
                >
                1 month    
                </Button>

                </ButtonGroup>

               

            </div>
        );
    }
}

ReactButtons.defaultProps = {};

ReactButtons.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    test_text: PropTypes.string,

    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * A label that will be printed when this component is rendered.
     */
    label: PropTypes.string.isRequired,

    /**
     * The value displayed in the input.
     */
    value: PropTypes.string,

    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
