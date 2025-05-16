/*
 * Copyright 2021, GeoSolutions Sas.
 * All rights reserved.
 *
 * This source code is licensed under the BSD-style license found in the
 * LICENSE file in the root directory of this source tree.
*/

import React from 'react';
import { connect } from 'react-redux';
import Message from "@mapstore/framework/components/I18N/Message";
import '@js/extension/assets/style.css';

import mygeonodeextension from '../reducers/mygeonodeextension';
import { activateExtension } from '../actions/mygeonodeextension';
import { getActiveExtension } from '../selectors/mygeonodeextension';

import { mapSelector } from '@mapstore/framework/selectors/map';

function Extension({
    active,
    onActivate,
    map
}) {

    const center = map?.center;
    const centerText = `x: ${center?.x} y: ${center?.y}`;
    return (
        <div className="extension">
            <Message msgId="extension.message" />
            {active ? centerText : null}
            <button onClick={() => onActivate(!active)}>
                { active ? 'Deactivate' : 'Activate' }
            </button>
        </div>
    );
}

const ConnectedExtension = connect((state) => ({
    active: getActiveExtension(state),
    map: mapSelector(state)
}), {
    onActivate: activateExtension
})(Extension);

export default {
    name: __MAPSTORE_EXTENSION_CONFIG__.name,
    component: ConnectedExtension,
    reducers: {
        mygeonodeextension
    },
    epics: {},
    containers: {}
};
