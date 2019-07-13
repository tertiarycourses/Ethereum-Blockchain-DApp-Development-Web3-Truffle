const Migrations = artifacts.require("Simple");

module.exports = function(deployer) {
  deployer.deploy(Migrations);
};
