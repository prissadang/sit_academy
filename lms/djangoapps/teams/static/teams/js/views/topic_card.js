/**
 * View for a topic card. Displays a Topic.
 */
;(function (define) {
    'use strict';
    define(['backbone', 'underscore', 'gettext', 'js/components/card/views/card'],
        function (Backbone, _, gettext, CardView) {
            var TeamCountDetailView = Backbone.View.extend({
                tagName: 'p',
                className: 'team-count',

                initialize: function () {
                    this.render();
                },

                render: function () {
                    var team_count = this.model.get('team_count');
                    this.$el.html(_.escape(interpolate(
                        ngettext('%(team_count)s Team', '%(team_count)s Teams', team_count),
                        {team_count: team_count},
                        true
                    )));
                    return this;
                }
            });

            var TopicCardView = CardView.extend({
                initialize: function () {
                    this.detailViews = [new TeamCountDetailView({ model: this.model })];
                    CardView.prototype.initialize.apply(this, arguments);
                },

                action: function (event) {
                    event.preventDefault();
                    this.router.navigate('topics/' + this.model.get('id'), {trigger: true});
                },

                configuration: 'square_card',
                cardClass: 'topic-card',
                title: function () { return this.model.get('name'); },
                description: function () { return this.model.get('description'); },
                details: function () { return this.detailViews; },
                actionClass: 'action-view',
                actionContent: function () {
                    var screenReaderText = _.escape(interpolate(
                        gettext('View Teams in the %(topic_name)s Topic'),
                        { topic_name: this.model.get('name') }, true
                    ));
                    return '<span class="sr">' + screenReaderText + '</span><i class="icon fa fa-arrow-right" aria-hidden="true"></i>';
                }
            });

            return TopicCardView;
        });
}).call(this, define || RequireJS.define);
