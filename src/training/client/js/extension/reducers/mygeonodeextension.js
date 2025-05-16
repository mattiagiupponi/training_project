
import { ACTIVATE_EXTENSION } from '../actions/mygeonodeextension';

function mygeonodeextension(state = {}, action) {
    switch (action.type) {
    case ACTIVATE_EXTENSION:
        return {
            ...state,
            active: action.active
        };
    default:
        return state;
    }
}

export default mygeonodeextension;
