{
  description = "A basic Nix flake with Python devShell, using venv";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-26.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { nixpkgs, flake-utils, ... }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = import nixpkgs { inherit system; };
      in
      {
        devShells.default = pkgs.mkShell {
          packages = with pkgs; [
            python3
            python3Packages.venvShellHook
          ];

          venvDir = ".venv";

          postVenvCreation = ''
            # Python tooling does not like SOURCE_DATE_EPOCH=1, which Nix can set
            unset SOURCE_DATE_EPOCH
            pip install -r requirements.txt
          '';
        };
      }
    );
}
