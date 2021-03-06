Ten thousand hours
=================
A very simple app inspired by Malcolm Gladwell's "Ten Thousand Hours" rule. It
helps you track how many hours you've spent doing various activities. None of
this is automatic - you need to tell it what you've done. All this app does is
give you summary statistics of your various activities.


## Developer environment

1. Make sure boot2docker is running (if on OSX): `boot2docker up`
1. Build the developer image: `make docker-create-tth-dev`
1. Run the dev server: `./scripts/run_tth_dev.sh`
1. Access the dev server by pointing your browser to: {your boot2docker ip}:8000
   * You can find your boot2docker ip with: `boot2docker ip`


## Deployment information ([Working site](http://10k-hour-ebextension-d.elasticbeanstalk.com/))

### Elastic Container Service

This is deployed using Amazon's Elastic Container Service.
* You need to have awscli version > 1.3 installed. This means you need to
  install the awscli using pip instead of brew.

1. First, build the docker images using Make. Remember to `rm` any previous
   docker tarballs, as otherwise they will hugely inflate the size of your
   containers.
1. Save the images as tarballs using `docker save <image_name> >
   <image_name>.tar`
1. `scp` the tarballs onto the container server using `scp -i
   ~/.ssh/rahul-eu-west.pem <tarball> ec2-user@52.16.47.112:~/`
1. Ssh into the container server and run `cat <tarball> | docker load` to load
   the images into docker.
1. Start the task on the container service using `aws ecs run-task --cluster
   default --task-definition ten_thousand_hours:<revision_num> --count 1`
   * The current revision number can be retrieved using `aws ecs
     list-task-definitions`

Updating an ECS task:
1. Update `ecs_task.json`
1. Run `aws ecs register-task-definition --cli-input-json
   file://$PWD/ecs_task.json`

Stopping ECS tasks:
1. View a list of running tasks using `aws ecs list-tasks`
1. Stop a specific task using `aws ecs stop-task <task-id>`
2. 

###Beanstalk

1. Install EB CLI
2. `eb init`
3. Choose ten_thousand_hours
4. `eb labs download`
5. Sync with Git & `eb deploy`
