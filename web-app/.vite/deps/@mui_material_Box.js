import {
  ClassNameGenerator_default,
  InitColorSchemeScript,
  createBox,
  createCssVarsProvider,
  createTheme,
  createTypography,
  generateUtilityClasses,
  identifier_default,
  require_jsx_runtime,
  styleFunctionSx_default
} from "./chunk-HVUPW2F7.js";
import {
  require_react
} from "./chunk-3VDXVL42.js";
import {
  require_prop_types
} from "./chunk-2PGV36BO.js";
import {
  __toESM
} from "./chunk-5WRI5ZAA.js";

// node_modules/@mui/material/esm/Box/Box.js
var import_prop_types2 = __toESM(require_prop_types(), 1);

// node_modules/@mui/material/esm/styles/ThemeProvider.js
var React4 = __toESM(require_react(), 1);

// node_modules/@mui/material/esm/styles/ThemeProviderNoVars.js
var React = __toESM(require_react(), 1);
var import_jsx_runtime = __toESM(require_jsx_runtime(), 1);

// node_modules/@mui/material/esm/styles/ThemeProviderWithVars.js
var React3 = __toESM(require_react(), 1);

// node_modules/@mui/material/esm/InitColorSchemeScript/InitColorSchemeScript.js
var React2 = __toESM(require_react(), 1);
var import_prop_types = __toESM(require_prop_types(), 1);
var import_jsx_runtime2 = __toESM(require_jsx_runtime(), 1);
var defaultConfig = {
  attribute: "data-mui-color-scheme",
  colorSchemeStorageKey: "mui-color-scheme",
  defaultLightColorScheme: "light",
  defaultDarkColorScheme: "dark",
  modeStorageKey: "mui-mode"
};
function InitColorSchemeScript2(props) {
  const {
    defaultMode = "system",
    defaultLightColorScheme = defaultConfig.defaultLightColorScheme,
    defaultDarkColorScheme = defaultConfig.defaultDarkColorScheme,
    modeStorageKey = defaultConfig.modeStorageKey,
    colorSchemeStorageKey = defaultConfig.colorSchemeStorageKey,
    attribute: initialAttribute = defaultConfig.attribute,
    colorSchemeNode = "document.documentElement",
    nonce
  } = props;
  return (0, import_jsx_runtime2.jsx)(InitColorSchemeScript, {
    defaultMode,
    defaultLightColorScheme,
    defaultDarkColorScheme,
    modeStorageKey,
    colorSchemeStorageKey,
    attribute: initialAttribute,
    colorSchemeNode,
    nonce
  });
}
true ? InitColorSchemeScript2.propTypes = {
  // ┌────────────────────────────── Warning ──────────────────────────────┐
  // │ These PropTypes are generated from the TypeScript type definitions. │
  // │ To update them, edit the TypeScript types and run `pnpm proptypes`. │
  // └─────────────────────────────────────────────────────────────────────┘
  /**
   * DOM attribute for applying a color scheme.
   * @default 'data-mui-color-scheme'
   * @example '.mode-%s' // for class based color scheme
   * @example '[data-mode-%s]' // for data-attribute without '='
   */
  attribute: import_prop_types.default.string,
  /**
   * The node (provided as string) used to attach the color-scheme attribute.
   * @default 'document.documentElement'
   */
  colorSchemeNode: import_prop_types.default.string,
  /**
   * localStorage key used to store `colorScheme`.
   * @default 'mui-color-scheme'
   */
  colorSchemeStorageKey: import_prop_types.default.string,
  /**
   * The default color scheme to be used in dark mode.
   * @default 'dark'
   */
  defaultDarkColorScheme: import_prop_types.default.string,
  /**
   * The default color scheme to be used in light mode.
   * @default 'light'
   */
  defaultLightColorScheme: import_prop_types.default.string,
  /**
   * The default mode when the storage is empty (user's first visit).
   * @default 'system'
   */
  defaultMode: import_prop_types.default.oneOf(["dark", "light", "system"]),
  /**
   * localStorage key used to store `mode`.
   * @default 'mui-mode'
   */
  modeStorageKey: import_prop_types.default.string,
  /**
   * Nonce string to pass to the inline script for CSP headers.
   */
  nonce: import_prop_types.default.string
} : void 0;

// node_modules/@mui/material/esm/styles/ThemeProviderWithVars.js
var import_jsx_runtime3 = __toESM(require_jsx_runtime(), 1);
var {
  CssVarsProvider: InternalCssVarsProvider,
  useColorScheme,
  getInitColorSchemeScript: deprecatedGetInitColorSchemeScript
} = createCssVarsProvider({
  themeId: identifier_default,
  // @ts-ignore ignore module augmentation tests
  theme: () => createTheme({
    cssVariables: true
  }),
  colorSchemeStorageKey: defaultConfig.colorSchemeStorageKey,
  modeStorageKey: defaultConfig.modeStorageKey,
  defaultColorScheme: {
    light: defaultConfig.defaultLightColorScheme,
    dark: defaultConfig.defaultDarkColorScheme
  },
  resolveTheme: (theme) => {
    const newTheme = {
      ...theme,
      typography: createTypography(theme.palette, theme.typography)
    };
    newTheme.unstable_sx = function sx(props) {
      return styleFunctionSx_default({
        sx: props,
        theme: this
      });
    };
    return newTheme;
  }
});

// node_modules/@mui/material/esm/styles/ThemeProvider.js
var import_jsx_runtime4 = __toESM(require_jsx_runtime(), 1);

// node_modules/@mui/material/esm/Box/boxClasses.js
var boxClasses = generateUtilityClasses("MuiBox", ["root"]);
var boxClasses_default = boxClasses;

// node_modules/@mui/material/esm/Box/Box.js
var defaultTheme = createTheme();
var Box = createBox({
  themeId: identifier_default,
  defaultTheme,
  defaultClassName: boxClasses_default.root,
  generateClassName: ClassNameGenerator_default.generate
});
true ? Box.propTypes = {
  // ┌────────────────────────────── Warning ──────────────────────────────┐
  // │ These PropTypes are generated from the TypeScript type definitions. │
  // │    To update them, edit the d.ts file and run `pnpm proptypes`.     │
  // └─────────────────────────────────────────────────────────────────────┘
  /**
   * @ignore
   */
  children: import_prop_types2.default.node,
  /**
   * The component used for the root node.
   * Either a string to use a HTML element or a component.
   */
  component: import_prop_types2.default.elementType,
  /**
   * The system prop that allows defining system overrides as well as additional CSS styles.
   */
  sx: import_prop_types2.default.oneOfType([import_prop_types2.default.arrayOf(import_prop_types2.default.oneOfType([import_prop_types2.default.func, import_prop_types2.default.object, import_prop_types2.default.bool])), import_prop_types2.default.func, import_prop_types2.default.object])
} : void 0;
var Box_default = Box;
export {
  boxClasses_default as boxClasses,
  Box_default as default
};
//# sourceMappingURL=@mui_material_Box.js.map
