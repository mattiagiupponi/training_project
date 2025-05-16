

export const ACTIVATE_EXTENSION = 'MY_GEONODE_EXTENSION:ACTIVATE_EXTENSION';

export const activateExtension = (active) => ({
    type: ACTIVATE_EXTENSION,
    active
});
